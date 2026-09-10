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

def application(repo, tag, categories, allow_prerelease=False):
    release = json.loads(subprocess.check_output([
        'gh', 'release', 'view', tag, '--repo', 'BearHero520/' + repo,
        '--json', 'tagName,isDraft,isPrerelease,assets,publishedAt,url'
    ], encoding='utf-8'))
    assert not release['isDraft'], 'Select a published release'
    assert allow_prerelease or not release['isPrerelease'], 'Select a stable release or explicitly allow the MiAir preview'
    assets = [a for a in release['assets'] if a['name'].endswith('.fpk')]
    versioned = [a for a in assets if tag.removeprefix('v') in a['name']]
    asset = (versioned or assets)[0]
    data = fetch(asset['url'])
    sha = hashlib.sha256(data).hexdigest()
    assert len(data) == asset['size'], 'Asset size mismatch'
    assert asset['digest'] == 'sha256:' + sha, 'GitHub digest mismatch'
    checksum_asset = next((a for a in release['assets'] if a['name'] == asset['name'] + '.sha256'), None)
    if checksum_asset:
        assert fetch(checksum_asset['url']).decode().split()[0].lower() == sha, 'Checksum file mismatch'
    else:
        checksum_asset = next(a for a in release['assets'] if a['name'] == 'SHA256SUMS')
        checksums = {line.split()[1].lstrip('*'): line.split()[0].lower() for line in fetch(checksum_asset['url']).decode('utf-8-sig').splitlines() if line.strip()}
        assert checksums.get(asset['name']) == sha, 'Checksum file mismatch'
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
    if release['isPrerelease']:
        app['desc'] = '【预览版】' + app['desc']
    assert app['run_as'] in ['root', 'package']
    assert app['install_type'] in ['', 'root']
    print(f'Validated {appname} {version}: {len(data)} bytes, SHA256 {sha}')
    return appname, app

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--toolbox-tag')
    parser.add_argument('--proxy-tag')
    parser.add_argument('--miair-tag')
    parser.add_argument('--allow-miair-preview', action='store_true')
    args = parser.parse_args()
    if not any([args.toolbox_tag, args.proxy_tag, args.miair_tag]):
        parser.error('Specify at least one release tag')
    source = json.loads((ROOT / 'fnpack.json').read_text(encoding='utf-8-sig'))
    apps = source['apps']
    for repo, tag, categories, allow_preview in [
        ('LLLED_FPK', args.toolbox_tag, ['系统工具', '硬件驱动'], False),
        ('fnos-reverse-proxy', args.proxy_tag, ['系统工具', '编程开发'], False),
        ('miair-plus', args.miair_tag, ['影音娱乐', '智能智控'], args.allow_miair_preview)
    ]:
        if tag:
            name, app = application(repo, tag, categories, allow_preview)
            apps[name] = app
    source['source_info']['description'] = '面向飞牛 fnOS 的 UGREEN 工具箱、反向代理与 MiAir Plus 应用。'
    encoded = json.dumps(source, ensure_ascii=False, indent=2) + '\n'
    assert len(encoded.encode('utf-8')) < 2 * 1024 * 1024
    (ROOT / 'fnpack.json').write_text(encoded, encoding='utf-8')

if __name__ == '__main__':
    main()
