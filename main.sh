git clone https://android.googlesource.com/toolchain/llvm
sudo apt-get install gcc-arm-linux-gnueabi
mkdir build
cd build
cmake ../llvm -DCMAKE_SYSTEM_NAME=arm-linux-gnueabi -DCMAKE_INSTALL_PREFIX=/system -DLLVM_HOST_TRIPLE=arm-linux-gnueabi
make -j128
tar -c * | gzip -9 > llvm-sysroot.tar.gz
