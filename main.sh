git clone https://android.googlesource.com/toolchain/llvm
sudo apt-get install gcc-arm-linux-gnueabihf
mkdir build
cd build
cmake ../llvm -DCMAKE_SYSTEM_NAME=Linux -DCMAKE_INSTALL_PREFIX=/system -DLLVM_HOST_TRIPLE=arm-linux-gnueabihf -DCMAKE_CXX_FLAGS='-march=armv7-a -mcpu=cortex-a52 -mfloat-abi=hard'
make -j128
tar -c * | gzip -9 > llvm-sysroot.tar.gz
