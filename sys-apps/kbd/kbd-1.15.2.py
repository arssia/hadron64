metadata = """
summary @ Keytable files and keyboard utilities
homepage @ ftp://ftp.altlinux.org/pub/people/legion/kbd/
license @ GPL
src_url @ ftp://ftp.altlinux.org/pub/people/legion/$name/$fullname.tar.gz
arch @ ~x86
"""

def prepare():
    patch(level=1)

def configure():
    raw_configure("--prefix=/usr",
            "--datadir=/lib/kbd")


