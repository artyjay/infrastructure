# Docker
Various Docker images for use in artyjay projects.

## Building

```
> cd <subdir>
> sudo ./build.sh
```

## Remote login
Images are stored on the Github Containers infrastructure, so a Personal Access Token should be generated on your GitHub account with `package write` access and add it to your environment as `GHCR_PAT`

Now login to the remote using:

```
> echo $GHCR_PAT | docker login ghcr.io -u artyjay --password-stdin
```

## Pushing

```
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