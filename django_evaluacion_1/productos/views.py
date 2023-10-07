from django.shortcuts import render, redirect

# Create your views here.


def index(request):

    return render(request, 'webproyecto_2/index.html')


def mouse(request):
    data = {"titulo": "Mouses Gamer Disponibles",
            "foto1": "mouse1.jpg",
            "foto2": "mouse2.jpg",
            "foto3": "mouse3.jpg",
            "producto1": "Logitech G Pro X Superlight",
            "producto2": "HyperX Pulsefire FPS Pro",
            "producto3": "Razer Cobra"}
    return render(request, 'webproyecto_2/producto.html', data)


def teclado(request):
    data = {"titulo": "Telclados Gamer Disponibles",
            "foto1": "teclado1.jpg",
            "foto2": "teclado2.jpg",
            "foto3": "teclado3.jpg",
            "producto1": "Redragon Kumara K552 RGB",
            "producto2": "Logitech G413 Carbon",
            "producto3": "Corsair K60 RGB PRO"}
    return render(request, 'webproyecto_2/producto.html', data)


def auris(request):
    data = {"titulo": "Audifonos Gamer Disponibles",
            "foto1": "auris1.jpeg",
            "foto2": "auris2.jpeg",
            "foto3": "auris3.jpeg",
            "producto1": "Razer Blackshark V2 Pro",
            "producto2": "Logitech G332",
            "producto3": "Redragon Pandora H350Rgb"}
    return render(request, 'webproyecto_2/producto.html', data)

def user(request):
    data = {"titulo": "Descripcion de usuario",
            "usuario": "Fabian Quezada.",
            "descripcion": "Estudiante analista programador en inacap temuco.",
            "interes": "Cliente habitual interesado en mouses gamer.",
            "foto1": "user1.jpg",
            "foto2": "user2.jpg",
            "foto3": "mouse1.jpg"}
    return render(request, 'webproyecto_2/user.html', data)


def mouse1(request):
    data = {"titulo": "Descripcion Logitech G Pro X Superlight",
            "foto1": "dselectro1.jpg",
            "producto1": "ESPECIFICACIONES FÍSICAS = Altura: 125,0 mm Ancho: 63,5 mm Profundidad: 40,0 mm Peso: <63 g ESPECIFICACIONES TÉCNICAS = Compatible con POWERPLAY Tecnología inalámbrica LIGHTSPEED Memoria integrada 1Las funciones avanzadas requieren el software Logitech G HUB, que se puede descargar desde logitechg.com/ghub Sistema de tensión de click Pies de PTFE sin aditivos 5 botones",
            "precio": "120.000"}
    return render(request, 'webproyecto_2/descripciones.html', data)

def mouse2(request):
    data = {"titulo": "Descripcion HyperX Pulsefire FPS Pro",
            "foto1": "dselectro2.jpg",
            "producto1": "Marca: HyperX / Tracking: PixArt / PMW-3389 [Óptico] / Cantidad de botones: 6 / DPI máximo: 16000 / Cableado: Alámbrico / Peso: 95 g / Tamaño: 128 x 42 x 71 mm. / DPI ajustable: Sí / Color: Negro",
            "precio": "20.500"}
    return render(request, 'webproyecto_2/descripciones.html', data)

def mouse3(request):
    data = {"titulo": "Descripcion Razer Cobra",
            "foto1": "dselectro3.jpg",
            "producto1": "USB tipo A / Tecnología de detección de movimientos / Óptico / Tipo de desplazamiento / Rueda / Cantidad de botones / 6 / Resolución de movimiento / 8500 DPI / Velocidad de seguimiento del ratón / 30 ips / Número de ruedas de desplazamiento / 1 / Aceleración (máx.) / 35 G",
            "precio": "36.000"}
    return render(request, 'webproyecto_2/descripciones.html', data)

def teclado1(request):
    data = {"titulo": "Descripcion Redragon Kumara K552 RGB",
            "foto1": "teclado1.jpg",
            "producto1": "Tipo de Switch / Outemu Blue, táctil con click audible, fuerza de actuación 50 gr / Teclas Multimedia / Si, a través de tecla FN / Teclas Macro Dedicadas / No / Bloqueo Tecla Windows / Si / Tamaño teclado / Tenkeyless (sin pad numérico) / Reposamuñecas / No / Retroiluminado / Si, RGB Chroma / Cable / Goma, reforzado. Soporta 12kg y 10000 flexiones. USB enchapado en oro y filtro anti interferencias / Matriz / 100% Anti-Ghosting con Full Key Rollover",
            "precio": "43.000"}
    return render(request, 'webproyecto_2/descripciones.html', data)

def teclado2(request):
    data = {"titulo": "Descripcion Logitech G413 Carbon",
            "foto1": "teclado2.jpg",
            "producto1": "Físicas / Altura: 132 mm / Anchura: 445 mm / Profundidad: 34 mm / Peso (sin cable): 1.105 g / Cable: 1,8 m / Switch Mecánico / ROMER G: / Duración: 70 millones de pulsaciones de teclas / Distancia de actuación: 1,5 mm / Fuerza de actuación: 45 g / Recorrido total: 3,2 mm",
            "precio": "93.000"}
    return render(request, 'webproyecto_2/descripciones.html', data)

def teclado3(request):
    data = {"titulo": "Descripcion Corsair K60 RGB PRO",
            "foto1": "teclado3.jpg",
            "producto1": "Peso: 0,88 kg / Lighting: RGB / Diseño del teclado: ES / Tasa de sondeo USB: 1000Hz / Switch: CHERRY® VIOLA / Matriz: 105 Teclas / Conectividad: cableado / Altura ajustable: Sí / Controles de medios: YN Sí / Tipo de teclado: Tamaño K60 / Familia de productos de teclado: K60 / Cambio de teclado: Full Key (NKRO) con 100% Anti-Ghosting / Factor de forma: Tamaño completo / Conectividad por cable: USB 3.0 o 3.1 tipo A / Memoria a bordo: Sí / Win Lock: Atajo FN / Control de medios: Atajos FN / Software CUE de teclado: Compatible / Tipo de cable: Caucho sin enredos / Panel táctil integrado: 441 mm x 137 mm x 35 mm / Material del cable del teclado: Caucho sin enredos",
            "precio": "123.000"}
    return render(request, 'webproyecto_2/descripciones.html', data)

def auris1(request):
    data = {"titulo": "Descripcion Razer Blackshark V2 Pro",
            "foto1": "auds1.jpeg",
            "producto1": "Condición del producto: Nuevo / Conectividad/conexión: Inalámbrico / Modelo: Blackshark V2 Pro 2023 Black / Dimensiones: 1 / Tipo de auricular: Over-Ear / Color: Negro",
            "precio": "220.000"}
    return render(request, 'webproyecto_2/descripciones.html', data)

def auris2(request):
    data = {"titulo": "Descripcion Logitech G332",
            "foto1": "auds2.jpeg",
            "producto1": "Tipo: Audífonos headset / Conectividad: Auxiliar / Condición del producto: Nuevo / Condición del producto: Nuevo / Producto Perecible: No / Resistente al agua: No / Potencia: No aplica",
            "precio": "93.000"}
    return render(request, 'webproyecto_2/descripciones.html', data)

def auris3(request):
    data = {"titulo": "Descripcion Redragon Pandora H350Rgb",
            "foto1": "auds3.jpeg",
            "producto1": "Tipo: Audífonos headset / Condición del producto: Nuevo / Modelo: 29REDHH350 / Producto Perecible: No / Conexión bluetooth: No / Impedancia: 32 / Entradas auxiliares de 3.5 mm: 1",
            "precio": "130.000"}
    return render(request, 'webproyecto_2/descripciones.html', data)




