#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9E18AA267DDB8DB4 (asarai@suse.de)
#
Name     : runc
Version  : 1.1.4
Release  : 75
URL      : https://github.com/opencontainers/runc/releases/download/v1.1.4/runc.tar.xz
Source0  : https://github.com/opencontainers/runc/releases/download/v1.1.4/runc.tar.xz
Source1  : https://github.com/opencontainers/runc/releases/download/v1.1.4/runc.tar.xz.asc
Summary  : CLI tool for spawning and running containers according to the OCI specification
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT
Requires: runc-bin = %{version}-%{release}
Requires: runc-license = %{version}-%{release}
BuildRequires : buildreq-golang
BuildRequires : pkgconfig(libseccomp)

%description
runc is a CLI tool for spawning and running containers on Linux according to
the OCI specification. It is a low level tool not designed with an end user in
mind. It is mostly employed by other higher level container software.

%package bin
Summary: bin components for the runc package.
Group: Binaries
Requires: runc-license = %{version}-%{release}

%description bin
bin components for the runc package.


%package license
Summary: license components for the runc package.
Group: Default

%description license
license components for the runc package.


%prep
%setup -q -n runc-1.1.4
cd %{_builddir}/runc-1.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661463494
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}  PREFIX=/usr


%install
export SOURCE_DATE_EPOCH=1661463494
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/runc
cp %{_builddir}/runc-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/runc/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
cp %{_builddir}/runc-%{version}/vendor/github.com/checkpoint-restore/go-criu/v5/LICENSE %{buildroot}/usr/share/package-licenses/runc/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/runc-%{version}/vendor/github.com/cilium/ebpf/LICENSE %{buildroot}/usr/share/package-licenses/runc/27a6200050717015f18fdbd39387845787ce81a9
cp %{_builddir}/runc-%{version}/vendor/github.com/containerd/console/LICENSE %{buildroot}/usr/share/package-licenses/runc/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/runc-%{version}/vendor/github.com/coreos/go-systemd/v22/LICENSE %{buildroot}/usr/share/package-licenses/runc/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/runc-%{version}/vendor/github.com/cpuguy83/go-md2man/v2/LICENSE.md %{buildroot}/usr/share/package-licenses/runc/b7a606730713ac061594edab33cf941704b4a95c
cp %{_builddir}/runc-%{version}/vendor/github.com/cyphar/filepath-securejoin/LICENSE %{buildroot}/usr/share/package-licenses/runc/8fb92f475d78da1315877a719c6856fc64531d30
cp %{_builddir}/runc-%{version}/vendor/github.com/docker/go-units/LICENSE %{buildroot}/usr/share/package-licenses/runc/3110e55750143a84918d7423febc9c83a55bc28c
cp %{_builddir}/runc-%{version}/vendor/github.com/godbus/dbus/v5/LICENSE %{buildroot}/usr/share/package-licenses/runc/994658c265db5dbf456fa6163905cc9c0b3bda46
cp %{_builddir}/runc-%{version}/vendor/github.com/moby/sys/mountinfo/LICENSE %{buildroot}/usr/share/package-licenses/runc/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/runc-%{version}/vendor/github.com/mrunalp/fileutils/LICENSE %{buildroot}/usr/share/package-licenses/runc/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
cp %{_builddir}/runc-%{version}/vendor/github.com/opencontainers/runtime-spec/LICENSE %{buildroot}/usr/share/package-licenses/runc/552b909d29bd260c886142a969b462c85f976dcd
cp %{_builddir}/runc-%{version}/vendor/github.com/opencontainers/selinux/LICENSE %{buildroot}/usr/share/package-licenses/runc/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/runc-%{version}/vendor/github.com/russross/blackfriday/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/runc/da34754c05d40ff81f91de8c1b85ea6e5503e21d
cp %{_builddir}/runc-%{version}/vendor/github.com/seccomp/libseccomp-golang/LICENSE %{buildroot}/usr/share/package-licenses/runc/cd87737b0bbdeee650f6a72ee61209863b1d827f
cp %{_builddir}/runc-%{version}/vendor/github.com/shurcooL/sanitized_anchor_name/LICENSE %{buildroot}/usr/share/package-licenses/runc/c111106ab0af1873aa6350f797759fe1519c8be1
cp %{_builddir}/runc-%{version}/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/runc/a1c7852c717fed2c9a0284ed112ea66013230da6
cp %{_builddir}/runc-%{version}/vendor/github.com/syndtr/gocapability/LICENSE %{buildroot}/usr/share/package-licenses/runc/a44bfde22babd7c7e1ccac9ca31f85a09358769f
cp %{_builddir}/runc-%{version}/vendor/github.com/urfave/cli/LICENSE %{buildroot}/usr/share/package-licenses/runc/62e85c543bad57a03eff756c0cfcb4bd26b77a4a
cp %{_builddir}/runc-%{version}/vendor/github.com/vishvananda/netlink/LICENSE %{buildroot}/usr/share/package-licenses/runc/f88291c879c4ee329bfa341b54eaedd29d3058cf
cp %{_builddir}/runc-%{version}/vendor/github.com/vishvananda/netns/LICENSE %{buildroot}/usr/share/package-licenses/runc/f88291c879c4ee329bfa341b54eaedd29d3058cf
cp %{_builddir}/runc-%{version}/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/runc/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/runc-%{version}/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/runc/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/runc-%{version}/vendor/google.golang.org/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/runc/74850a25a5319bdddc0d998eb8926c18bada282b
%make_install PREFIX=/usr

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/runc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/runc/172ca3bbafe312a1cf09cfff26953db2f425c28e
/usr/share/package-licenses/runc/27a6200050717015f18fdbd39387845787ce81a9
/usr/share/package-licenses/runc/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/runc/3110e55750143a84918d7423febc9c83a55bc28c
/usr/share/package-licenses/runc/552b909d29bd260c886142a969b462c85f976dcd
/usr/share/package-licenses/runc/62e85c543bad57a03eff756c0cfcb4bd26b77a4a
/usr/share/package-licenses/runc/74850a25a5319bdddc0d998eb8926c18bada282b
/usr/share/package-licenses/runc/8fb92f475d78da1315877a719c6856fc64531d30
/usr/share/package-licenses/runc/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
/usr/share/package-licenses/runc/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/runc/994658c265db5dbf456fa6163905cc9c0b3bda46
/usr/share/package-licenses/runc/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/runc/a44bfde22babd7c7e1ccac9ca31f85a09358769f
/usr/share/package-licenses/runc/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/runc/c111106ab0af1873aa6350f797759fe1519c8be1
/usr/share/package-licenses/runc/cd87737b0bbdeee650f6a72ee61209863b1d827f
/usr/share/package-licenses/runc/d3b7a70b03b43d4e7205d178100581923a0baad2
/usr/share/package-licenses/runc/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/runc/da34754c05d40ff81f91de8c1b85ea6e5503e21d
/usr/share/package-licenses/runc/f88291c879c4ee329bfa341b54eaedd29d3058cf
