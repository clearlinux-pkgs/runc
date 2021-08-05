Name     : runc
Version  : 1.0.1
Release  : 49
URL      : https://github.com/opencontainers/runc/releases/download/v1.0.1/runc.tar.xz
Source0  : https://github.com/opencontainers/runc/releases/download/v1.0.1/runc.tar.xz
Summary  : CLI tool for spawning and running containers according to the OCF specification.
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : go
BuildRequires : glibc-staticdev
BuildRequires : libseccomp-dev

%global library_path github.com/opencontainers/
%global goroot /usr/lib/golang
%global runc_version %{version}

%description
runc is a CLI tool for spawning and running containers according to the OCF specification.

%package dev
Summary: dev components for the runc package.
Group: Development

%description dev
dev components for the runc package.

%prep
%setup -q -n runc-%runc_version

%build
export GOPATH=$HOME/go AUTO_GOPATH=1
mkdir -p $HOME/go/src/github.com/opencontainers
ln -s /builddir/build/BUILD/runc-%runc_version $HOME/go/src/github.com/opencontainers/runc
pushd $HOME/go/src/github.com/opencontainers/runc
make V=1 %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
install -d -p %{buildroot}/usr/bin
install -p -m 755 runc %{buildroot}/usr/bin
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
/usr/bin/runc

%files dev
%defattr(-,root,root,-)
%{goroot}/src/%{library_path}/*
