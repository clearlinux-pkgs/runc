Name     : runc
Version  : 0
Release  : 16
URL      : https://github.com/opencontainers/runc/archive/3f2f8b84a77f73d38244dd690525642a72156c64.tar.gz
Source0  : https://github.com/opencontainers/runc/archive/3f2f8b84a77f73d38244dd690525642a72156c64.tar.gz
Summary  : CLI tool for spawning and running containers according to the OCF specification.
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : go
BuildRequires : glibc-staticdev
BuildRequires : libseccomp-dev

%global library_path github.com/opencontainers/
%global commit 3f2f8b84a77f73d38244dd690525642a72156c64
%global goroot /usr/lib/golang

%description
runc is a CLI tool for spawning and running containers according to the OCF specification.

%package dev
Summary: dev components for the runc package.
Group: Development

%description dev
dev components for the runc package.

%prep
%setup -q -n runc-%{commit}

%build
export GOPATH=/go AUTO_GOPATH=1
mkdir -p /go/src/github.com/opencontainers
ln -s /builddir/build/BUILD/runc-%{commit} /go/src/github.com/opencontainers/runc
pushd /go/src/github.com/opencontainers/runc
make V=1 %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
install -d -p %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}
# Copy all *.go, *.s and *.proto files
install -d -p %{buildroot}%{goroot}/src/%{library_path}/
for ext in go s proto; do
	for file in $(find . -iname "*.$ext" | grep -v "^./Godeps") ; do
		install -d -p %{buildroot}%{goroot}/src/%{library_path}/$(dirname $file)
		cp -pav $file %{buildroot}%{goroot}/src/%{library_path}/$file
	done
done

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%files dev
%defattr(-,root,root,-)
%{goroot}/src/%{library_path}/*
