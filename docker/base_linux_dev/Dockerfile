FROM ubuntu:bionic
LABEL maintainer="R.Johnson"

## Install packages
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    binutils \
    ca-certificates \
    clang-7 \
    clang-format-7 \
    curl \
    g++-8-multilib \
    git \
    gnupg \
    lld-7 \
    lldb-7 \
    nasm \
    ninja-build \
    python3 \
    python3-pip \
    tar \
    wget \
    xz-utils \
 && rm -rf /var/lib/apt/lists/*

## Compiler configuration - prefer Clang default
RUN update-alternatives --install /usr/bin/gcc   gcc   /usr/bin/gcc-8   100 --slave /usr/bin/g++     g++     /usr/bin/g++-8 \
 && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-7 100 --slave /usr/bin/clang++ clang++ /usr/bin/clang++-7 \
 && update-alternatives --install /usr/bin/cc    cc    /usr/bin/clang   100 --slave /usr/bin/c++     c++     /usr/bin/clang++
 && update-alternatives --install /usr/bin/cc    cc    /usr/bin/gcc     100 --slave /usr/bin/c++     c++     /usr/bin/g++ \

## CMake installation
RUN wget -q -O - https://github.com/Kitware/CMake/releases/download/v3.13.4/cmake-3.13.4-Linux-x86_64.tar.gz | tar -xvz --strip-components 1 -C /usr