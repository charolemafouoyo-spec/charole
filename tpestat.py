def f(x):
    return x**2-4
#dichotomie
def dichotomie(f ,a ,b, seuil=0.1):

    if f(a) * f(b) >= 0:
       return None

       while abs(b - a) >= seuil:
           s = (a + b) / 2
           if f(a) * f(s) < 0:
               b = s
           else:
               a = s
       return (a+b) / 2

    function_input
    b = float
    print("entrez la fonction f(x) en terme de x: ")
    print("entrez la valeur de a: ")
    print("entrez la valeur de b: ")

resultat = dichotomie(f, 1, 2, seuil=0.1)

if resultat is not None:
    print(f"la racine trouvee est:{resultat}")
else:
    print("aucune racine trouvee dans cet intervalle.")

#balayage
def balay(f, a, b, eps):
    if eps <= 0:
        raise valueError("eps doit etre > 0")
    if a >= b:
        raise valueError("a doit etre < b")
    x = a
    while x + eps <= b:
        fx = f(x)
        fxp = f(x + eps)
        if fx * fxp <= 0:
            return(x + (x + eps))

        x += eps
        raise valueError("aucune intervalle contenant une racine trouve dans [a,b]")

#methodesequente
def sequente(f, a, tol=1e-8, max_iter=1000):
    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        raise valueError("les valeurs f(a) et  f(b) doivent etre de signes opposes.")
    for n in range(1, max_iter + 1):
        denom = (fb - fa)
        if denom == 0:
            s = (a + b) / 2.0
            fs = f(s)
            return s, n, fs
            s = (a * fb - b * fa)/denom
            fs = f(s)
            if abs(fs) <= tol or abs(b - a) <= tol:
                return s, n, fs
            if fs * fb < 0:
                a, fa = s, fs
            else:
                 b, fb = s, fs
            return s, max_iter, fs

#methodenewton
def newton(f, df, x0, tol=1e-8, max_iter=100):

    n = x0
    dfn = df(n)
    eps_deriv = 1e-12
    if abs(dfn) < eps_deriv:
        raise valueError("derivee trop proche de zero au depart.")
    s = n - f(n) / dfn
    for i in range (max_iter):
        if abs(s-n) <= tol:
            return s
        n = s
        dfn = df(n)
        if abs(dfn) < eps_deriv:
            raise valueError('derivee trop proche de zero (iteration{i}).')
        s = n - f(n) / dfn
    return s













