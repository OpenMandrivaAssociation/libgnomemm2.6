%define version 2.18.0
%define release %mkrel 1

%define gtkmm_version 2.4.0
%define libgnome_version 2.6.0

%define major 1

%define pkgname libgnomemm
%define api_version 2.6
%define libname_orig	%mklibname gnomemm %api_version
%define libname		%mklibname gnomemm %api_version %{major}

Summary: 	A C++ wrapper for libgnome
Name: 		%{pkgname}%{api_version}
Version: 	%{version}
Release: 	%{release}
License: 	LGPL
Group: 		System/Libraries
URL: 		http://gtkmm.sourceforge.net/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
BuildRequires:	gtkmm2.4-devel >= %{gtkmm_version}
BuildRequires:	libgnome2-devel >= %{libgnome_version}
Buildrequires:	doxygen

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


%package -n %{libname}-devel
Summary:	Development files for libgnome C++ wrapper
Group: 		Development/GNOME and GTK+
Provides:	%name-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	gtkmm2.4-devel >= %{gtkmm_version}
Requires:	libgnome2-devel >= %{libgnome_version}

%description -n %{libname}-devel
This package contains all necessary files, including libraries and headers,
that C++ programmers will need to develop applications which use %{pkgname},
the C++ interface to libgnome library.

It is necessary when compiling applications which use %{pkgname} as well.

%prep
%setup -q -n %{pkgname}-%{version}
touch configure

%build
%configure2_5x --enable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %buildroot -name \*.la|xargs chmod 644

### Build doc
pushd docs/reference
  perl -pi -e 's/^(HAVE_DOT.*=) YES/$1 NO/' Doxyfile
  make all
popd

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}


%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING README
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-, root, root)
%doc docs/reference/html COPYING ChangeLog NEWS
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{pkgname}-%{api_version}

###########################################################################

