%global tl_name texlive-es
%global tl_revision 78678

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	TeX Live manual (Spanish)
Group:		Publishing
URL:		https://www.ctan.org/pkg/texlive-es
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-es.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-es.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeX Live manual (Spanish)

