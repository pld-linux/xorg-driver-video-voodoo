Summary:	X.org video driver for Voodoo1 and Voodoo2 video adapters
Summary(pl):	Sterownik obrazu X.org dla kart graficznych Voodoo1 i Voodoo2
Name:		xorg-driver-video-voodoo
Version:	1.0.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-voodoo-%{version}.tar.bz2
# Source0-md5:	031a1e64b4bddb7ea57e0df3aa0c54ee
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Voodoo1 and Voodoo2 video adapters.

%description -l pl
Sterownik obrazu X.org dla kart graficznych Voodoo1 i Voodoo2.

%prep
%setup -q -n xf86-video-voodoo-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/voodoo_drv.so
%{_mandir}/man4/voodoo.4x*
