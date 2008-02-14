%define name mbw
%define version 1.1
%define release %mkrel 1

Summary: Memory bandwidth benchmark
Name: %name
Version: %version
Release: %release
License: LGPL
Source: %{name}.tar.bz2
Group: System/Kernel and hardware
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:http://freshmeat.net/redir/mbw/64534/url_homepage/mbw

%description
Test memory copy bandwidth (single thread).
Switch off swap or make sure array size does not exceed available free RAM.

%prep
%setup -n %{name}

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 mbw %{buildroot}%{_bindir}/mbw
install -m 644 mbw.1 %{buildroot}%{_mandir}/man1/mbw.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/mbw
%doc %{_mandir}/man1/mbw.1*

%changelog
