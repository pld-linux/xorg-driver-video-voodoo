Summary:	X.org video driver for Voodoo1 and Voodoo2 video adapters
Summary(pl):	Sterownik obrazu X.org dla kart graficznych Voodoo1 i Voodoo2
Name:		xorg-driver-video-voodoo
Version:	1.1.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-voodoo-%{version}.tar.bz2
# Source0-md5:	bc878e795688b49a595b355482d27174
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
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
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/voodoo_drv.so
%{_mandir}/man4/voodoo.4*
