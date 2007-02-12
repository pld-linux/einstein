Summary:	An implementation of Albert Einstein's puzzle
Summary(pl.UTF-8):	Implementacja gry logicznej Alberta Einsteina
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
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The game goal is to open all cards in square of 6x6 cards. For this, a
number of hints describing relations between card positions are given.

%description -l pl.UTF-8
Celem gry jest odsłonięcie wszystkich kart w kwadracie 6x6 za pomocą
podpowiedzi opisujących relacje pomiędzy poszczególnymi kartami.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	OPTIMIZE="%{rpmcflags}"

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
