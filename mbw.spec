%define name mbw
%define version 1.1
%define release 6

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
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-5mdv2011.0
+ Revision: 620307
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1-4mdv2010.0
+ Revision: 430003
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.1-3mdv2009.0
+ Revision: 252136
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 1.1-1mdv2008.1
+ Revision: 168107
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Fri May 04 2007 Erwan Velu <erwan@mandriva.org> 1.1-1mdv2008.0
+ Revision: 22498
- Import mbw

