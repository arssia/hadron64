metadata = """
summary @ GNU database library
homepage @ http://www.gnu.org/software/gdbm/gdbm.html
license @ GPL-2
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def prepare():
    patch(level=1)

    #system("libtoolize --force --copy")
    #aclocal()
    #autoconf()

def configure():
    conf("--disable-static")

def install():
    raw_install("INSTALL_ROOT=%s" % install_dir)
    raw_install("INSTALL_ROOT=%s includedir=/usr/include/gdbm" % install_dir, "install-compat")
