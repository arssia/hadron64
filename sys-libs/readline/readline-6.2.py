metadata = """
summary @ GNU readline library
homepage @ http://tiswww.case.edu/php/chet/readline/rltop.html
license @ GPL
src_url @ http://ftp.gnu.org/gnu/readline/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/ncurses
"""

def prepare():
    system("sed -i 's|-Wl,-rpath,$(libdir) ||g' support/shobj-conf")

def configure():
    raw_configure("--prefix=/usr",
            "--libdir=/lib")

def build():
    make("SHLIB_LIBS=-lncurses")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insfile("%s/inputrc" % filesdir, "/etc/inputrc")

    makedirs("/usr/lib")

    move("%s/lib/libreadline.a" % install_dir, "/usr/lib/libreadline.a")
    move("%s/lib/libhistory.a" % install_dir, "/usr/lib/libhistroy.a")

    #cd("%s/usr/lib" % install_dir)

    makesym("/lib/libreadline.so.6", "/usr/lib/libreadline.so")
    makesym("/lib/libhistory.so.6", "/usr/lib/libhistory.so")
