%define url_ver %(echo %{version}|cut -d. -f1,2)

%define pkgname	libgnomemm
%define api	2.6
%define major	1
%define libname	%mklibname gnomemm %{api} %{major}
%define devname	%mklibname -d gnomemm %{api}

Summary:	A C++ wrapper for libgnome
Name:		%{pkgname}%{api}
Version:	2.30.0
Release:	12
License:	LGPLv2+
Group:		System/Libraries
Url:		http://gtkmm.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomemm/%{url_ver}/%{pkgname}-%{version}.tar.bz2
BuildRequires:	doxygen
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libgnome-2.0)

%description
The %{pkgname} library provides a C++ wrapper for libgnome library.
It is a subpackage of the gnomemm project, which provides C++ binding
of various GNOME libraries.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}

%description -n %{libname}
The %{pkgname} library provides a C++ wrapper for libgnome library.
It is a subpackage of the gnomemm project, which provides C++ binding
of various GNOME libraries.

%package -n %{devname}
Summary:	Development files for libgnome C++ wrapper
Group: 		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains all necessary files, including libraries and headers,
that C++ programmers will need to develop applications which use %{pkgname},
the C++ interface to libgnome library.

%prep
%setup -qn %{pkgname}-%{version}

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING README
%{_libdir}/libgnomemm-%{api}.so.%{major}*

%files -n %devname
%doc COPYING ChangeLog NEWS docs/reference/html
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{pkgname}-%{api}

