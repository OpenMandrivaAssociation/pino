Summary:	A fast, easy and free Twitter and Identi.ca client
Name:		pino
Version:	0.2.11
Release:	1
Group:		Networking/Other
License:	LGPLv3+
URL:		https://code.google.com/p/pino-twitter/
Source0:	http://pino-twitter.googlecode.com/files/%{name}-%{version}.tar.bz2

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	vala
BuildRequires:	waf
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(webkit-1.0)

%description
Pino is a simple and fast microblogging client for Linux desktop. It
supports Twitter and Iidenti.ca.

%prep
%setup -q

%build
CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" waf configure --prefix=%{_prefix}
waf build -v %{?_smp_mflags}

%install
waf install --destdir=%{buildroot} -p

# Remove docs from /usr/share/doc/pino
rm -rf %{buildroot}%{_datadir}/doc/pino

%find_lang %{name}

# Desktop file validate
desktop-file-validate %{buildroot}%{_datadir}/applications/pino.desktop

%files -f %{name}.lang
%doc AUTHORS README
%{_bindir}/pino
%{_datadir}/applications/pino.desktop
%{_datadir}/icons/hicolor/scalable/*/*.svg
%dir %{_datadir}/pino
%{_datadir}/pino/icons/*
%{_datadir}/pino/templates/*.tpl
%{_datadir}/indicators/messages/applications/pino

