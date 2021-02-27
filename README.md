# Docker
Various Docker images for use in artyjay projects.

## Building

```
> cd <subdir>
> sudo ./build.sh
```

## Pushing

Images are stored on the Github Containers infrastructure

Generate a Personal Access Token with `package write` access

```
> export CR_PAT=<Generated PAT>
> echo $CR_PAT | docker login ghcr.io -u artyjay --password-stdin
> docker push ghcr.io/artyjay/<subdir>:latest
```

## Using

If pulling from remote:

```
> docker pull ghcr.io/artyjay/<subdir>:latest
> docker run --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -v <mount host path>:/host -w /host -it ghcr.io/artyjay/<subdir>:latest
```

If building locally first before using:

```
> cd <subdir>
> ./run <mount host path>
```