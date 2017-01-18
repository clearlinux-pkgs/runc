Name     : runc
Version  : 50a19c6ff828c58e5dab13830bd3dacde268afe5
Release  : 10
URL      : https://github.com/opencontainers/runc/archive/50a19c6ff828c58e5dab13830bd3dacde268afe5.tar.gz
Source0  : https://github.com/opencontainers/runc/archive/50a19c6ff828c58e5dab13830bd3dacde268afe5.tar.gz
Summary  : CLI tool for spawning and running containers according to the OCF specification.
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : go
BuildRequires : glibc-staticdev
BuildRequires : libseccomp-dev

%global gopath /usr/lib/golang
%global library_path github.com/opencontainers/

%description
runc is a CLI tool for spawning and running containers according to the OCF specification.

%package dev
Summary: dev components for the runc package.
Group: Development

%description dev
dev components for the runc package.

%prep
%setup -q -n runc-50a19c6ff828c58e5dab13830bd3dacde268afe5

%build
mkdir -p src/github.com/opencontainers
ln -s $(pwd) src/github.com/opencontainers/runc
export GOPATH=$(pwd):%{gopath}
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -d -p %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}
# Copy all *.go, *.s and *.proto files
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for ext in go s proto; do
	for file in $(find . -iname "*.$ext" | grep -v "^./Godeps") ; do
		install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
		cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
	done
done

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%files dev
%defattr(-,root,root,-)
%{gopath}/src/%{library_path}/*
