%define name	chpax
%define version	0.7
%define release 8

Name:		%{name}
Summary:	Tool that allows PaX flags to be modified on a per-binary basis
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.7-autotools.patch.bz2
URL:		https://pax.grsecurity.net/
Group:		System/Configuration/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	Public Domain
BuildRequires:	autoconf2.5 automake

%description
A tool that allows PaX flags to be modified on a per-binary basis. PaX is part
of common security-enhancing kernel patches, like GrSecurity. Your system needs
to be running an appropriately patched kernel, like the one provided by the
kernel-secure package, for this program to have any effect.

%prep
%setup -q
%patch0 -p1 -b .autotools

%build 
aclocal
autoheader
autoconf
automake --foreign -a
%configure 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root,0755) 
%{_mandir}/man1/chpax.1*
%{_sbindir}/chpax
%defattr(644,root,root,0755)
%doc README ChangeLog



%changelog
* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7-7mdv2011.0
+ Revision: 627770
- don't force the usage of automake1.7

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7-6mdv2011.0
+ Revision: 617035
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.7-5mdv2010.0
+ Revision: 424837
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.7-4mdv2009.0
+ Revision: 222089
- fix calling autoheader
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix autoconf-2.5x path
- import chpax

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Aug 02 2006 Lenny Cartier <lenny@mandriva.com> 0.7-3mdv2007.0
- rebuild

* Tue Jan 03 2005 Lenny Cartier <lenny@mandriva.com> 0.7-2mdk
- rebuild

* Wed Jul 28 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.7-1mdk
- 0.7
- regenerate P0

* Tue Jan 06 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.6-1mdk
- from Omer Shenker <chpax@omershenker.net> :
	- New version

* Tue Dec 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.5-1mdk
- from Omer Shenker <chpax@omershenker.net> :
	- Specfile for Mandrake
	- gz to bz2 compression

