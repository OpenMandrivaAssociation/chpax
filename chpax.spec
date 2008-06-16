%define name	chpax
%define version	0.7
%define release %mkrel 4

Name:		%{name}
Summary:	Tool that allows PaX flags to be modified on a per-binary basis
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.7-autotools.patch.bz2
URL:		http://pax.grsecurity.net/
Group:		System/Configuration/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	Public Domain
BuildRequires:	autoconf2.5 automake1.7

%description
A tool that allows PaX flags to be modified on a per-binary basis. PaX is part
of common security-enhancing kernel patches, like GrSecurity. Your system needs
to be running an appropriately patched kernel, like the one provided by the
kernel-secure package, for this program to have any effect.

%prep
%setup -q
%patch0 -p1 -b .autotools

%build 
aclocal-1.7
autoheader-2.5x
autoconf
automake-1.7 --foreign -a
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

