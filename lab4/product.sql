PGDMP         9            
    {            lab4    14.9    14.9     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16912    lab4    DATABASE     e   CREATE DATABASE lab4 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Kazakhstan.1251';
    DROP DATABASE lab4;
                postgres    false            �            1259    16932    product    TABLE     �   CREATE TABLE public.product (
    product_id integer NOT NULL,
    product_name character varying(1000) NOT NULL,
    measure numeric(1000,0) NOT NULL
);
    DROP TABLE public.product;
       public         heap    postgres    false            �          0    16932    product 
   TABLE DATA           D   COPY public.product (product_id, product_name, measure) FROM stdin;
    public          postgres    false    210   Y       a           2606    16938    product product_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (product_id);
 >   ALTER TABLE ONLY public.product DROP CONSTRAINT product_pkey;
       public            postgres    false    210            �   �   x�-��N�@D뽏A�ۜ����D�("DD�2N�%�`�f��Y�5s3�o�`�.�p�$��B��gt�I�����5���6�)��lqE��m��@w�� ^�Yc=2�I��k���NrMe)�d�/�'� 1iH���tz�Yt�kw�|3��gM���C�f"%�W�a[�N�̛49�XVY[4�z���S+��J�x�=�(Z����-��/��	!��6��     