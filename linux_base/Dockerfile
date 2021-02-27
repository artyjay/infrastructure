FROM ubuntu:bionic
LABEL maintainer="Bob Johnson"

# Install packages ensuring gcc & clang versions are latest desired
RUN apt-get update \ 
 && DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends \
apt-utils \
ca-certificates \
gpg-agent \
software-properties-common \
tzdata \
wget \
 && add-apt-repository -y ppa:ubuntu-toolchain-r/test \
 && wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && add-apt-repository "deb http://apt.llvm.org/bionic/   llvm-toolchain-bionic-11  main" \
 && apt-get update \ 
 && DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends \
automake \
build-essential \
binutils \
clang-11 \
clangd-11 \
clang-format-11 \
curl \
g++-10 \
g++-10-multilib \
gdb-multiarch \
git \
gnupg \
libtool \
libbz2-dev \
libffi-dev \
liblzma-dev \
libncurses5-dev \
libncursesw5-dev \
libreadline-dev \
libsqlite3-dev \ 
libssl-dev \
lldb-11 \
lld-11 \
m4 \
nasm \
ninja-build \
pkg-config \
python-openssl \
sudo \
tar \
tk-dev \
xz-utils \
zlib1g-dev \
 && apt-get autoremove -y \
 && apt-get clean all \
 && rm -rf /var/lib/apt/lists/*

# Remove alternatives GCC installation setup as will manual setup next to allow
# trivial swapping between Windows/Linux
# Compiler configuration - prefer Clang default
RUN update-alternatives --remove-all c++ \
 && update-alternatives --remove-all cc \ 
 && update-alternatives --install /usr/bin/gcc          gcc          /usr/bin/gcc-10          100 --slave /usr/bin/g++     g++     /usr/bin/g++-10 \
 && update-alternatives --install /usr/bin/clang        clang        /usr/bin/clang-11        100 --slave /usr/bin/clang++ clang++ /usr/bin/clang++-11 \
 && update-alternatives --install /usr/bin/cc           cc           /usr/bin/clang           100 --slave /usr/bin/c++     c++     /usr/bin/clang++ \
 && update-alternatives --install /usr/bin/cc           cc           /usr/bin/gcc             100 --slave /usr/bin/c++     c++     /usr/bin/g++ \
 && update-alternatives --install /usr/bin/clang-format clang-format /usr/bin/clang-format-11 100

# CMake installation
RUN wget -q -O - https://github.com/Kitware/CMake/releases/download/v3.19.6/cmake-3.19.6-Linux-x86_64.tar.gz | tar -xvz --strip-components 1 -C /usr

# User setup
RUN groupadd 1001 -g 1001 \
 && groupadd 1000 -g 1000 \
 && groupadd 2000 -g 2000 \
 && groupadd 999 -g 999 \
 && useradd -ms /bin/bash builder -g 1001 -G 1000,2000,999 \
 && printf "builder:builder" | chpasswd \
 && adduser builder sudo \
 && printf "builder ALL= NOPASSWD: ALL\\n" >> /etc/sudoers

USER builder
WORKDIR /home/builder/

# py-env installation
RUN curl https://pyenv.run | bash \
 && export PATH="/home/builder/.pyenv/bin:$PATH" \
 && eval "$(pyenv init -)" \
 && eval "$(pyenv virtualenv-init -)"

# Python & Conan installation
COPY requirements.txt /tmp_files/
COPY generate_conan_profiles.py /tmp_files/
ENV PYENV_ROOT /home/builder/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN pyenv install 3.9.2 \  
 && pyenv global 3.9.2 \
 && pip install --upgrade pip \
 && pip install --no-cache-dir -r /tmp_files/requirements.txt \
 && mkdir -p /home/builder/.conan \
 && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
 && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc \
 && conan remote add artyjay https://artyjay.jfrog.io/artifactory/api/conan/conan-local \
 && python /tmp_files/generate_conan_profiles.py