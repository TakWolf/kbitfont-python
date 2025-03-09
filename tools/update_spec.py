import httpx

from tools import project_root_dir


def main():
    hash_name = 'ee1627fa7a8b40754aeff13a479305dd0a4df3bd'
    src_root_dir = project_root_dir.joinpath('bitsnpicas-spec', 'bitsnpicas', 'src', 'main', 'java', 'com', 'kreative', 'bitsnpicas')
    for file_dir, _, file_names in src_root_dir.walk():
        for file_name in file_names:
            if not file_name.endswith('.java'):
                continue
            file_path = file_dir.joinpath(file_name)
            url = f'https://raw.githubusercontent.com/kreativekorp/bitsnpicas/{hash_name}/main/java/BitsNPicas/src/com/kreative/bitsnpicas/{file_path.relative_to(src_root_dir)}'.replace('\\', '/')

            response = httpx.get(url)
            assert response.is_success and 'text/plain' in response.headers['Content-Type']
            file_path.write_text(response.text, 'utf-8')
            print(f"Update: '{file_path}'")


if __name__ == '__main__':
    main()
