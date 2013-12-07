# revision 30307
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-htmlxml
Epoch:		1
Version:	20131013
Release:	4
Summary:	HTML/SGML/XML support
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-htmlxml.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-collection-fontsrecommended
Requires:	texlive-collection-latex
Requires:	texlive-jadetex
Requires:	texlive-passivetex
Requires:	texlive-tex4ht
Requires:	texlive-xmltex

%description
Packages to convert LaTeX to XML/HTML, and typset XML/SGML.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
