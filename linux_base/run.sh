#!/bin/sh

# Launch docker mounting host folder
MOUNT_PATH=$1

if [ "$MOUNT_PATH" = "" ]; then
	SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
	MOUNT_PATH="$(readlink -f $SCRIPTPATH)"
fi

echo "\nLaunching:        artyjay/linux_base"
echo "Host folder:      $MOUNT_PATH"
echo "Container folder: /host\n"

docker run --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -v $MOUNT_PATH:/host -w /host -it artyjay/linux_base
