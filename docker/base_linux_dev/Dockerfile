
## docker file with build env setup for stuff I want to make

## gcc8 - 
## clang 7
## setup alternatives
## setup python
## setup python env
## pip some stuff
## setup git
## cmake

FROM ubuntu:bionic
LABEL maintainer="Rob Johnson"

## Common tools
RUN apt-get -qq update \
 && apt-get -qq install -y --no-install-recommends \
    git \
    binutils \
    nasm \
    ninja-build \
    xz-utils \
    curl \
    tar \
    ca-certificates \
    wget \
    gnupg \
    python3 \
 && rm -rf /var/lib/apt/lists/*

## CMake
RUN wget -q -O - https://github.com/Kitware/CMake/releases/download/v3.13.4/cmake-3.13.4-Linux-x86_64.tar.gz | tar -xvz --strip-components 1 -C /usr

## GCC
RUN apt-get -qq update \
 && apt-get -qq install -y --no-install-recommends g++-8-multilib \
 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 100 --slave /usr/bin/g++ g++ /usr/bin/g++-8 \
 && rm -rf /var/lib/apt/lists/*

## Clang 7
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && apt-get -qq update \
 && apt-get install -y --no-install-recommends \
    clang-7 \
    lldb-7 \
    lld-7 \
    clang-format-7 \
 && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-7 100 --slave /usr/bin/clang++ clang++ /usr/bin/clang++-7 \
 && rm -rf /var/lib/apt/lists/*

## Compilers
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/gcc 100 --slave /usr/bin/c++ c++ /usr/bin/g++ \
 && update-alternatives --install /usr/bin/cc cc /usr/bin/clang 100 --slave /usr/bin/c++ c++ /usr/bin/clang++
