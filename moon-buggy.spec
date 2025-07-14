Summary:	Drive some car across the moon
Summary(pl.UTF-8):	Jazda samochodem po księżycu
Name:		moon-buggy
Version:	1.0.51
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://seehuhn.de/data/%{name}-%{version}.tar.gz
# Source0-md5:	bfe23ef5cfa838ac261eee34ea5322f3
Patch0:		%{name}-info.patch
URL:		http://seehuhn.de/comp/moon-buggy.html
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

%description -l pl.UTF-8
Moon-buggy jest grą tekstową, w której jeździsz pewnym rodzajem
samochodu po powierzchni księżyca. Niestety, są tam niebezpieczne
kratery. Na szczęście samochód może przez nie przeskakiwać!

%prep
%setup -q
%patch -P0 -p1

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

%{__rm} $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ANNOUNCE AUTHORS ChangeLog NEWS README TODO
%attr(2755,root,games) %{_bindir}/moon-buggy
%{_infodir}/*.info*
%{_mandir}/man6/*
%attr(775,root,games) %dir /var/games/moon-buggy
%attr(664,root,games) %ghost /var/games/moon-buggy/*
