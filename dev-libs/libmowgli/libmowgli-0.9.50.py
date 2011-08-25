metadata = """
summary @ Performance and usability-oriented extensions to C
homepage @ http://www.atheme.org/project/mowgli
license @ custom
src_url @ http://distfiles.atheme.org/$fullname.tar.bz2
arch @ ~x86
options @ examples
"""

def configure():
    conf(
    config_enable("examples"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "README")
