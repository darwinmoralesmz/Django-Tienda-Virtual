from django.test import TestCase
from .models import Estado, Genero, Pais, Perfiles, Region, Comuna, UsersMetadata, ProductoCategoria, Proveedor, Producto

class ModelCreationTestCase(TestCase):
    def test_create_estado(self):
        estado = Estado.objects.create(nombre="Activo")
        self.assertEqual(estado.nombre, "Activo")
        print(f"Estado creado: {estado.nombre}")

    def test_create_genero(self):
        genero = Genero.objects.create(nombre="Masculino")
        self.assertEqual(genero.nombre, "Masculino")
        print(f"Genero creado: {genero.nombre}")

    def test_create_pais(self):
        pais = Pais.objects.create(nombre="Chile")
        self.assertEqual(pais.nombre, "Chile")
        print(f"País creado: {pais.nombre}")

    def test_create_perfiles(self):
        perfil = Perfiles.objects.create(nombre="Administrador")
        self.assertEqual(perfil.nombre, "Administrador")
        print(f"Perfil creado: {perfil.nombre}")

    def test_create_region(self):
        region = Region.objects.create(nombre="Región Metropolitana")
        self.assertEqual(region.nombre, "Región Metropolitana")
        print(f"Región creada: {region.nombre}")

    def test_create_comuna(self):
        region = Region.objects.create(nombre="Región Metropolitana")
        comuna = Comuna.objects.create(nombre="Santiago", region=region)
        self.assertEqual(comuna.nombre, "Santiago")
        print(f"Comuna creada: {comuna.nombre}")

from django.test import TestCase

from django.contrib.auth.models import User

class ModelRelationshipTestCase(TestCase):
    def test_users_metadata_relationships(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        estado = Estado.objects.create(nombre="Activo")
        genero = Genero.objects.create(nombre="Masculino")
        perfil = Perfiles.objects.create(nombre="Administrador")
        pais = Pais.objects.create(nombre="Chile")
        region = Region.objects.create(nombre="Región Metropolitana")
        comuna = Comuna.objects.create(nombre="Santiago", region=region)

        users_metadata = UsersMetadata.objects.create(
            user=user,
            estado=estado,
            genero=genero,
            perfiles=perfil,
            pais=pais,
            comuna=comuna,
            slug="testuser",
            correo="test@example.com",
            telefono="123456789",
            direccion="Calle Falsa 123"
        )
        print(f"Usuario relacionado: {users_metadata.user}")

        self.assertEqual(users_metadata.user, user)
        self.assertEqual(users_metadata.estado, estado)
        self.assertEqual(users_metadata.genero, genero)
        self.assertEqual(users_metadata.perfiles, perfil)
        self.assertEqual(users_metadata.pais, pais)
        self.assertEqual(users_metadata.comuna, comuna)

class ModelUpdateTestCase(TestCase):
    def test_update_estado(self):
        estado = Estado.objects.create(nombre="Activo")
        estado.nombre = "Inactivo"
        estado.save()
        self.assertEqual(estado.nombre, "Inactivo")

    def test_update_producto(self):
        estado = Estado.objects.create(nombre="Disponible")
        categoria = ProductoCategoria.objects.create(nombre="Electrónicos")
        proveedor = Proveedor.objects.create(nombre="Proveedor Test")
        producto = Producto.objects.create(
            nombre="Producto Test",
            descripcion="Descripción Test",
            producto_categoria=categoria,
            proveedor=proveedor,
            estado=estado,
            precio=100,
            precio_antes=150,
            sku="123",
            stock=10
        )
        producto.precio = 90
        print(f"Estado actualizado: {estado.nombre}")
        producto.save()
        self.assertEqual(producto.precio, 90)

class ModelDeletionTestCase(TestCase):
    def test_delete_estado(self):
        estado = Estado.objects.create(nombre="Activo")
        estado_id = estado.id
        estado.delete()
        with self.assertRaises(Estado.DoesNotExist):
            Estado.objects.get(id=estado_id)
        print(f"Estado Eliminado: {estado.id}")

    def test_delete_producto(self):
        estado = Estado.objects.create(nombre="Disponible")
        categoria = ProductoCategoria.objects.create(nombre="Electrónicos")
        proveedor = Proveedor.objects.create(nombre="Proveedor Test")
        producto = Producto.objects.create(
            nombre="Producto Test",
            descripcion="Descripción Test",
            producto_categoria=categoria,
            proveedor=proveedor,
            estado=estado,
            precio=100,
            precio_antes=150,
            sku="123",
            stock=10
        )
        producto_id = producto.id
        producto.delete()
        with self.assertRaises(Producto.DoesNotExist):
            Producto.objects.get(id=producto_id)





