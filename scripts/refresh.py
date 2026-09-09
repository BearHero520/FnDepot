"""Refresh FnDepot metadata from explicitly selected, published GitHub releases."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'https://github.com/BearHero520/FnDepot'

def fetch(url):
    with urllib.request.urlopen(url, timeout=90) as response:
        return response.read()

def application(repo, tag, categories):
    release = json.loads(subprocess.check_output([
        'gh', 'release', 'view', tag, '--repo', 'BearHero520/' + repo,
        '--json', 'tagName,isDraft,isPrerelease,assets,publishedAt,url'
    ], encoding='utf-8'))
    assert not release['isDraft'] and not release['isPrerelease'], 'Select a published stable release'
    assets = [a for a in release['assets'] if a['name'].endswith('.fpk')]
    versioned = [a for a in assets if tag.removeprefix('v') in a['name']]
    asset = (versioned or assets)[0]
    data = fetch(asset['url'])
    sha = hashlib.sha256(data).hexdigest()
    assert len(data) == asset['size'], 'Asset size mismatch'
    assert asset['digest'] == 'sha256:' + sha, 'GitHub digest mismatch'
    checksum_asset = next(a for a in release['assets'] if a['name'] == asset['name'] + '.sha256')
    assert fetch(checksum_asset['url']).decode().split()[0].lower() == sha, 'Checksum file mismatch'
    with tarfile.open(fileobj=io.BytesIO(data)) as archive:
        def member(name):
            entry = next(m for m in archive.getmembers() if m.name.removeprefix('./') == name)
            return archive.extractfile(entry).read()
        manifest = dict(line.split('=', 1) for line in member('manifest').decode('utf-8').splitlines() if '=' in line)
        manifest = {k.strip(): v.strip() for k, v in manifest.items()}
        privilege = json.loads(member('config/privilege'))
        icon = member('ICON_256.PNG')
    appname, version, platform = [manifest[k] for k in ['appname', 'version', 'platform']]
    assert tag == 'v' + version
    assert platform in ['x86', 'arm', 'all']
    assert len(icon) < 500 * 1024 and icon.startswith(b'\x89PNG\r\n\x1a\n')
    icon_path = ROOT / 'assets' / 'icons' / (appname + '.png')
    icon_path.parent.mkdir(parents=True, exist_ok=True)
    icon_path.write_bytes(icon)
    homepage = 'https://github.com/BearHero520/' + repo
    app = {
        'display_name': manifest['display_name'], 'desc': manifest['desc'],
        'platform': [platform], 'categories': categories,
        'icon_url': 'https://raw.githubusercontent.com/BearHero520/FnDepot/main/assets/icons/' + icon_path.name,
        'readme_url': 'https://raw.githubusercontent.com/BearHero520/' + repo + '/' + tag + '/README.md',
        'bug_report_url': homepage + '/issues',
        'maintainer': manifest['maintainer'], 'maintainer_url': homepage,
        'run_as': privilege['defaults']['run-as'],
        'install_type': manifest.get('install_type', ''), 'is_docker': False,
        'service_port': manifest.get('service_port', ''),
        'releases': {version: {
            'changelog': manifest.get('changelog', ''),
            'updated_at': release['publishedAt'],
            'os_min_version': manifest.get('os_min_version', ''),
            'packages': {platform: {'download_url': asset['url'], 'sha256': sha, 'size': len(data)}}
        }}
    }
    assert app['run_as'] in ['root', 'package']
    assert app['install_type'] in ['', 'root']
    print(f'Validated {appname} {version}: {len(data)} bytes, SHA256 {sha}')
    return appname, app

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--toolbox-tag', required=True)
    parser.add_argument('--proxy-tag', required=True)
    args = parser.parse_args()
    apps = dict([
        application('LLLED_FPK', args.toolbox_tag, ['系统工具', '硬件驱动']),
        application('fnos-reverse-proxy', args.proxy_tag, ['系统工具', '编程开发'])
    ])
    source = {'schema_version': '2', 'source_info': {
        'name': 'BearHero 应用源', 'author': 'BearHero520', 'homepage': SOURCE,
        'description': '面向飞牛 fnOS 的 UGREEN 工具箱与反向代理应用。'
    }, 'apps': apps}
    encoded = json.dumps(source, ensure_ascii=False, indent=2) + '\n'
    assert len(encoded.encode('utf-8')) < 2 * 1024 * 1024
    (ROOT / 'fnpack.json').write_text(encoded, encoding='utf-8')

if __name__ == '__main__':
    main()
