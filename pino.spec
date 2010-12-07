Name:		pino
Version:	0.2.10
Release:	%mkrel 2
Summary:	A fast, easy and free Twitter and Identi.ca client

Group:		Networking/Other
License:	LGPLv3+
URL:		http://code.google.com/p/pino-twitter/
Source0:	http://pino-twitter.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:	waf vala intltool gettext desktop-file-utils
BuildRequires:	libgee-devel libnotify-devel libsoup-devel libxml2-devel
BuildRequires:	webkitgtk-devel unique-devel gtkspell-devel

%description
Pino is a simple and fast microblogging client for Linux desktop. It
supports Twitter and Iidenti.ca.

%prep
%setup -q

%build
CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" waf configure --prefix=%{_prefix}
waf build -v %{?_smp_mflags}


%install
rm -rf %{buildroot}
waf install --destdir=%{buildroot} -p

# Remove docs from /usr/share/doc/pino
rm -rf %{buildroot}%{_datadir}/doc/pino

# Locale files
%find_lang %{name}

# Desktop file validate
desktop-file-validate %{buildroot}%{_datadir}/applications/pino.desktop


%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS README
%{_bindir}/pino
%{_datadir}/applications/pino.desktop
%{_datadir}/icons/hicolor/scalable/*/*.svg
%dir %{_datadir}/pino
%{_datadir}/pino/icons/*
%{_datadir}/pino/templates/*.tpl
%{_datadir}/indicators/messages/applications/pino
