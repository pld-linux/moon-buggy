Summary:	Drive some car across the moon
Summary(pl):	Jazda samochodem po ksiê¿ycu
Name:		moon-buggy
Version:	0.5.52
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://www.hangout.de/moon-buggy/%{name}-%{version}.tar.gz
# Source0-md5:	1d081d3210c59b376f6a9f332aea1a04
Patch0:		%{name}-info.patch
URL:		http://www.hangout.de/moon-buggy/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sharedstatedir		/var/games

%description
Moon-buggy is a simple character graphics game, where you drive some
kind of car across the moon's surface. Unfortunately there are
dangerous craters there. Fortunately your car can jump over them!

%description -l pl
Moon-buggy jest gr± tekstow±, w której je¼dzisz pewnym rodzajem
samochodu po powierzchni ksiê¿yca. Niestety, s± tam niebezpieczne
kratery. Na szczê¶cie samochód mo¿e przez nie przeskakiwaæ!

%prep
%setup -q
%patch -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

:> $RPM_BUILD_ROOT/var/games/moon-buggy/mbscore

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ANNOUNCE AUTHORS ChangeLog NEWS README TODO
%attr(2755,root,games) %{_bindir}/*
%{_infodir}/*.info*
%{_mandir}/man6/*
%attr(775,root,games) %dir /var/games/moon-buggy
%attr(664,root,games) %ghost /var/games/moon-buggy/*
