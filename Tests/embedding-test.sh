# This file contains tests for embedded highlighting inside here-documents.

echo <<HTML
<head>
	<title>This is embedded HTML.</title>
<head>
HTML

echo <<HTML
<body with-cutoff="true"
HTML

echo <<FOO
<p>Something that's <em>not</em> HTML.</p>
FOO
