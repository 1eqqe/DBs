PGDMP     #    8            
    {            lab4    14.9    14.9     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16912    lab4    DATABASE     e   CREATE DATABASE lab4 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Kazakhstan.1251';
    DROP DATABASE lab4;
                postgres    false            �            1259    16913    bludo    TABLE       CREATE TABLE public.bludo (
    bludo_id integer NOT NULL,
    bludo_type character varying(1000) NOT NULL,
    weight_bludo numeric(1000,0) NOT NULL,
    recipe character varying(1000) NOT NULL,
    callories numeric(1000,0) NOT NULL,
    carbs_capacity numeric(1000,0) NOT NULL
);
    DROP TABLE public.bludo;
       public         heap    postgres    false            �          0    16913    bludo 
   TABLE DATA           f   COPY public.bludo (bludo_id, bludo_type, weight_bludo, recipe, callories, carbs_capacity) FROM stdin;
    public          postgres    false    209   �       a           2606    16919    bludo bludo_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.bludo
    ADD CONSTRAINT bludo_pkey PRIMARY KEY (bludo_id);
 :   ALTER TABLE ONLY public.bludo DROP CONSTRAINT bludo_pkey;
       public            postgres    false    209            �   S  x�eSI��@<w��`�e���1��3��~ ��ay,�_����2�AKwWeeee�N�J�3��k7N'OX�u��A��t�S�A�9�+����.:�e7.����^����n\A�Fw��t!��X�b��N>Ki�e�ԯ�"��q�w��/�)�u֭�t�w�ҁUk�}Nb��\�'�&��5����8֮(
'"��A>J��XD�Fy��Ao4�Wz{E(Գu)�3��� 8ɞ�.�I����oT�����P�&�n��W���������}k�����8����}b�R.Q���H?F[4�~n\XK�a��O}A���c\�|���ph��ܧ��!'}ɹA}�ų�EK�R�8-&�`��zG �º�~��������g�{Y��2Z-�1�kĝ�WGH4����ͪȳ��*����ӑ������gO�y�h�/�,qS$e�(�cw��)k�HL�-60�@��+� ��*�^���3.i6���. ��]�a-��\S�ß��.��B��T��0�s�2��#��m*\�-� t��j���0�1?�g�gC�#��m't�(�;�b��}�q}     