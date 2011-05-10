metadata = """
summary @ Lists open files for running Unix processes
homepage @ http://people.freebsd.org/~abe/
license @ custom
src_url @ ftp://sunsite.ualberta.ca/pub/Mirror/lsof/$name_$version.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

srcdir = "%s_%s" % (name, version)

def configure():
    system("tar xf %s_%s_src.tar" % (name, version))
    cd("%s_%s_src" % (name, version))
    system("sed -i 's|/\* #define\tHASSECURITY\t1 \*/|#define\tHASSECURITY\t1|' \
            dialects/linux/machine.h")
    system("./Configure -n linux")

def build():
    cd("%s_%s_src" % (name, version))
    make()

def install():
    cd("%s_%s_src" % (name, version))
    insexe("lsof", "/usr/sbin/lsof")