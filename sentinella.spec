Summary:	System monitor
Name:		sentinella
Version:	0.9.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://sentinella.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/0.9.x/%{name}-%version.tar.xz

BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	qt4-devel
BuildRequires:	%{_lib}sysactivity-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel

%description
Application that monitors your system activity and, when a condition is met, 
takes the action that you've chosen.
While monitoring your CPU, memory, hard drive and network usage, Sentinella 
can be programmed to take specific actions when set-points for utilization 
or time are met. It can power off, reboot or hibernate your system, 
kill an active process, throw an alarm or execute any command.

Sentinella integrates perfectly with KDE4 and will work on many *nix systems.

%prep
%setup -q

%build
%cmake_kde4 
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-kde

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="X-MandrivaLinux-System-Monitoring" \
	--dir %{buildroot}%{_kde_datadir}/applications/kde4/ \
	%{buildroot}%{_kde_datadir}/applications/kde4/*

%files -f %{name}.lang
%doc CHANGELOG COPYING
%{_bindir}/sentinella
%{_datadir}/applications/kde4/%{name}.desktop
%{_datadir}/sounds/Sentinella
%{_iconsdir}/hicolor/*/apps/%{name}.*



%changelog
* Tue May 29 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.9.0-1
+ Revision: 801027
- imported package sentinella

