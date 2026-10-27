document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".arithmatex").forEach(node => {
    const value = node.textContent.trim();
    const display = value.startsWith(String.fromCharCode(92) + "[");
    const tex = value.slice(2, -2);
    try { katex.render(tex, node, {displayMode: display, throwOnError: true, trust: false}); node.dataset.mathRendered = "true"; }
    catch (error) { node.dataset.mathError = error.message; console.error(error); }
  });
});
