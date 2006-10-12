Summary:	An implementation of Albert Einstein's puzzle
Summary(pl):	Implementacja gry logicznej Alberta Einsteina
Name:		einstein
Version:	2.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://games.flowix.com/files/einstein/%{name}-%{version}-src.tar.gz
# Source0-md5:	c1d98e761c10af63f03462ead625f80c
Patch0:		%{name}-makefile.patch
URL:		http://games.flowix.com/
BuildRequires:	SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The game goal is to open all cards in square of 6x6 cards. For this, a number of hints describing relations between card positions are given.

%description -l pl
Celem gry jest ods³oniêcie wszystkich kart w kwadracie 6x6 za pomoc± podpowiedzi opisuj±cych relacje pomiêdzy poszczególnymi kartami.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
