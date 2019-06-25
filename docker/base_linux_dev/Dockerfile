FROM ubuntu:bionic
LABEL maintainer="R.Johnson"

## Install packages
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    ca-certificates \
    gnupg \
    wget \
 && wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
 && apt-get install -y --no-install-recommends \
    binutils \
    clang-7 \
    clang-format-7 \
    curl \
    g++-8-multilib \
    gdb-multiarch \
    git \
    lld-7 \
    lldb-7 \
    nasm \
    ninja-build \
    pkg-config \
    python3 \
    python3-pip \
    sudo \
    tar \
    xz-utils \
 && rm -rf /var/lib/apt/lists/*

## Compiler configuration - prefer Clang default
RUN update-alternatives --install /usr/bin/gcc   gcc   /usr/bin/gcc-8   100 --slave /usr/bin/g++     g++     /usr/bin/g++-8 \
 && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-7 100 --slave /usr/bin/clang++ clang++ /usr/bin/clang++-7 \
 && update-alternatives --install /usr/bin/cc    cc    /usr/bin/clang   100 --slave /usr/bin/c++     c++     /usr/bin/clang++ \
 && update-alternatives --install /usr/bin/cc    cc    /usr/bin/gcc     100 --slave /usr/bin/c++     c++     /usr/bin/g++

## CMake installation
RUN wget -q -O - https://github.com/Kitware/CMake/releases/download/v3.14.5/cmake-3.14.5-Linux-x86_64.tar.gz | tar -xvz --strip-components 1 -C /usr

## Update default python to python3.
RUN rm -f /usr/bin/python \
 && update-alternatives --install /usr/bin/python python /usr/bin/python3 100 \
 && update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 100

## Conan
RUN python -m pip install --upgrade pip \
 && pip install setuptools \
 && pip install wheel \
 && pip install conan==1.16.1 \
 && conan profile new default --detect \
 && conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan
