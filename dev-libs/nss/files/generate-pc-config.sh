#!/bin/bash

# Generate nss.pc and nss-config from nss.pc.in and nss-config.in
# Ozan Caglayan, 2010

# this script was modified for Hadron and lpms by purak

LIBDIR="/usr/lib/nss"
PREFIX="/usr"
EXEC_PREFIX="/usr"
INCLUDEDIR="/usr/include/nss"

PKGCONFIG="mozilla/dist/pkgconfig/nss.pc.in"
NSSCONFIG="mozilla/dist/pkgconfig/nss-config.in"

NSS_VMAJOR=`grep "#define.*NSS_VMAJOR" mozilla/security/nss/lib/nss/nss.h | awk '{print $3}'`
NSS_VMINOR=`grep "#define.*NSS_VMINOR" mozilla/security/nss/lib/nss/nss.h | awk '{print $3}'`
NSS_VPATCH=`grep "#define.*NSS_VPATCH" mozilla/security/nss/lib/nss/nss.h | awk '{print $3}'`

#NSS_VMAJOR=`cat security/nss/lib/nss/nss.h | grep "#define.*NSS_VMAJOR" | awk '{print $3}'`
#NSS_VMINOR=`cat security/nss/lib/nss/nss.h | grep "#define.*NSS_VMINOR" | awk '{print $3}'`
#NSS_VPATCH=`cat security/nss/lib/nss/nss.h | grep "#define.*NSS_VPATCH" | awk '{print $3}'`
NSS_VERSION="$NSS_VMAJOR.$NSS_VMINOR.$NSS_VPATCH"
NSPR_VERSION=`nspr-config --version`

echo "NSS_VMAJOR: $NSS_VMAJOR"
echo "NSS_VMINOR: $NSS_VMINOR"
echo "NSS_VPATCH: $NSS_VPATCH"
echo "NSS_VERSION: $NSS_VERSION"

# Setup nss-config
cat $NSSCONFIG | sed    -e "s,@prefix@,$PREFIX,g" \
                        -e "s,@MOD_MAJOR_VERSION@,$NSS_VMAJOR,g" \
                        -e "s,@MOD_MINOR_VERSION@,$NSS_VMINOR,g" \
                        -e "s,@MOD_PATCH_VERSION@,$NSS_VPATCH,g" \
                        > mozilla/dist/pkgconfig/nss-config

# Set executable bit
chmod 755 mozilla/dist/pkgconfig/nss-config

# Setup pkgconfig file
cat $PKGCONFIG | sed    -e "s,@libdir@,$LIBDIR,g" \
                        -e "s,@prefix@,$PREFIX,g" \
                        -e "s,@exec_prefix@,$EXEC_PREFIX,g" \
                        -e "s,@includedir@,$INCLUDEDIR,g" \
                        -e "s,@NSS_VERSION@,$NSS_VERSION,g" \
                        -e "s,@NSPR_VERSION@,$NSPR_VERSION,g" \
                        > mozilla/dist/pkgconfig/nss.pc


# Clear .in files
rm -rf $PKGCONFIG $NSSCONFIG
