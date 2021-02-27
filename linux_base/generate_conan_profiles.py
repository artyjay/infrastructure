import os
import itertools
import pathlib
import subprocess
import sys

conan_profile_template = '''[settings]
{settings}
[options]
[build_requires]
[env]
{env}
'''

os_arch_types = [
    {
        'name': 'linux-x86_64',
        'settings':
        {
            'os': 'Linux',
            'os_build': 'Linux',
            'arch': 'x86_64',
            'arch_build': 'x86_64',
        }
    }
]

compiler_types = [
    {
        'name': 'clang',
        'settings':
        {
            'compiler': 'clang',
            'compiler.version': '11',
            'compiler.libcxx': 'libstdc++11'
        },
        'env':
        {
            'CC': 'clang-11',
            'CXX': 'clang-11',
            'AR': 'llvm-ar-11',
            'NM': 'llvm-nm-11',
            'LD': 'llvm-link-11',
            'STRIP': 'llvm-strip-11'
        }
    },
    {
        'name': 'gcc',
        'settings':
        {
            'compiler': 'gcc',
            'compiler.version': '10',
            'compiler.libcxx': 'libstdc++11'
        },
        'env':
        {
            'CC': 'gcc-10',
            'CXX': 'g++-10',
            'AR': 'gcc-ar-10',
            'NM': 'gcc-nm-10'
        }
    }
]

build_types = [
    {
        'name': 'debug',
        'settings':
        {
            'build_type': 'Debug'
        }
    },
    {
        'name': 'release',
        'settings':
        {
            'build_type': 'Release'
        }
    }
]

profiles_path = os.path.join(pathlib.Path.home(), '.conan', 'profiles')
print(f'Conan profiles folder {profiles_path}')
os.makedirs(profiles_path, exist_ok=True)

# Run permutations to generation profiles
for profile in itertools.product(os_arch_types, compiler_types, build_types):
    os_arch = profile[0]
    compiler = profile[1]
    build = profile[2]

    os_arch_name = os_arch['name']
    compiler_name = compiler['name']
    build_name = build['name']

    profile_settings = {}
    profile_env = {}

    for entry in profile:
        entry_settings = entry.get('settings', {})
        entry_env = entry.get('env', {})

        profile_settings.update(entry_settings)
        profile_env.update(entry_env)

    def values_string(entry_dict):
        return '\n'.join(map(lambda kv: f'{kv[0]}={kv[1]}', entry_dict.items()))

    profile_name         = f'{os_arch_name}-{compiler_name}-{build_name}'
    profile_settings_str = values_string(profile_settings)
    profile_env_str      = values_string(profile_env)
    
    profile = conan_profile_template.format(settings=profile_settings_str,
                                            env=profile_env_str)

    print(f'Generating profile {profile_name}')

    profile_path = os.path.join(profiles_path, profile_name)

    with open(profile_path, 'wt') as profile_file:
        profile_file.write(profile)