/**
 * Realiza una petición POST al endpoint /login con credenciales de usuario,
 * luego procesa la respuesta JSON y muestra una alerta con el resultado.
 */
fetch('http://localhost:5000/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ nombre: 'usuario', contraseña: '1234' })
})
.then(res => res.json())
.then(data => {
  if (data.error) {
    alert(data.error);
  } else {
    alert('Bienvenido ' + data.nombre);
  }
});
