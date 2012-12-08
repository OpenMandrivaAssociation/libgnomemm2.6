%define major 1

%define pkgname libgnomemm
%define api_version 2.6
%define libname_orig	%mklibname gnomemm %{api_version}
%define libname		%mklibname gnomemm %{api_version} %{major}
%define develname %mklibname -d gnomemm %{api_version}

Summary:	A C++ wrapper for libgnome
Name:		%{pkgname}%{api_version}
Version:	2.30.0
Release:	6
License:	LGPLv2+
Group:		System/Libraries
URL:		http://gtkmm.sourceforge.net/
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libgnome-2.0)
BuildRequires:	doxygen

%description
The %{pkgname} library provides a C++ wrapper for libgnome library.
It is a subpackage of the gnomemm project, which provides C++ binding
of various GNOME libraries.


%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Provides:	%{libname_orig} = %{version}-%{release}

%description -n %{libname}
The %{pkgname} library provides a C++ wrapper for libgnome library.
It is a subpackage of the gnomemm project, which provides C++ binding
of various GNOME libraries.


%package -n %{develname}
Summary:	Development files for libgnome C++ wrapper
Group: 		Development/GNOME and GTK+
Provides:	%name-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	pkgconfig(gtkmm-2.4)
Requires:	pkgconfig(libgnome-2.0)

%description -n %{develname}
This package contains all necessary files, including libraries and headers,
that C++ programmers will need to develop applications which use %{pkgname},
the C++ interface to libgnome library.

It is necessary when compiling applications which use %{pkgname} as well.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING README
%{_libdir}/libgnomemm-%{api_version}.so.%{major}*

%files -n %develname
%doc COPYING ChangeLog NEWS docs/reference/html
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{pkgname}-%{api_version}

###########################################################################




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.30.0-3mdv2011.0
+ Revision: 661469
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 2.30.0-2mdv2011.0
+ Revision: 602555
- rebuild

* Mon Mar 29 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528766
- update to new version 2.30.0

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-2mdv2010.1
+ Revision: 520842
- rebuilt for 2010.1

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446586
- update to new version 2.28.0

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.26.0-2mdv2010.0
+ Revision: 425555
- rebuild

* Mon Mar 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355971
- update to new version 2.26.0

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286531
- new version
- update license

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.22.0-2mdv2009.0
+ Revision: 222750
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Mar 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 182992
- new version

* Thu Jan 17 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 154091
- fix build
- new version
- update file list

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 2.20.0-2mdv2008.1
+ Revision: 150617
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 85534
- new version
- new devel name
- bump deps


* Sat Mar 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 140350
- new version

* Tue Jan 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-2mdv2007.1
+ Revision: 103072
- Import libgnomemm2.6

* Tue Jan 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-2mdv2007.1
- Rebuild

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New release 2.16.0

* Thu Aug 03 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.14.0-3mdv2007.0
- rebuild w/o selinux on x86_64

* Tue Jul 18 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.0-2mdv2007.0
- Rebuild to drop obsolete howl dependency

* Tue Apr 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.0-1mdk
- New release 2.14.0

* Fri Jan 27 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.2-1mdk
- New release 2.12.2
- use mkrel

* Thu Nov 17 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.1-1mdk
- New release 2.12.1

* Sun Oct 09 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.0-1mdk
- New release 2.12.0

* Tue May 10 2005 Götz Waschk <waschk@mandriva.org> 2.10.0-2mdk
- fix devel provides

* Mon Mar 07 2005 Götz Waschk <waschk@linux-mandrake.com> 2.10.0-1mdk
- source URL
- New release 2.10

* Wed Jan 05 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.0-2mdk 
- Rebuild with latest howl

* Wed Nov 10 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.0-1mdk
- fix source URL
- New release 2.8.0

* Mon Jun 21 2004 Abel Cheung <deaddog@deaddog.org> 2.6.0-2mdk
- Rebuild with new g++
- reenable libtoolize

* Fri Apr 30 2004 Abel Cheung <deaddog@deaddog.org> 2.6.0-1mdk
- New major release

* Fri Apr 30 2004 Abel Cheung <deaddog@deaddog.org> 2.0.1-2mdk
- Rebuild

