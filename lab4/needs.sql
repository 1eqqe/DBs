PGDMP     1    8            
    {            lab4    14.9    14.9 	    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16912    lab4    DATABASE     e   CREATE DATABASE lab4 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Kazakhstan.1251';
    DROP DATABASE lab4;
                postgres    false            �            1259    16939    needs    TABLE     �   CREATE TABLE public.needs (
    bludo_id integer NOT NULL,
    product_id integer NOT NULL,
    product_volume character varying(1000) NOT NULL
);
    DROP TABLE public.needs;
       public         heap    postgres    false            �          0    16939    needs 
   TABLE DATA           E   COPY public.needs (bludo_id, product_id, product_volume) FROM stdin;
    public          postgres    false    211   �       a           2606    16945    needs needs_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.needs
    ADD CONSTRAINT needs_pkey PRIMARY KEY (product_volume);
 :   ALTER TABLE ONLY public.needs DROP CONSTRAINT needs_pkey;
       public            postgres    false    211            b           2606    16946    needs bludo_id    FK CONSTRAINT     t   ALTER TABLE ONLY public.needs
    ADD CONSTRAINT bludo_id FOREIGN KEY (bludo_id) REFERENCES public.bludo(bludo_id);
 8   ALTER TABLE ONLY public.needs DROP CONSTRAINT bludo_id;
       public          postgres    false    211            c           2606    16951    needs product_id    FK CONSTRAINT     |   ALTER TABLE ONLY public.needs
    ADD CONSTRAINT product_id FOREIGN KEY (product_id) REFERENCES public.product(product_id);
 :   ALTER TABLE ONLY public.needs DROP CONSTRAINT product_id;
       public          postgres    false    211            �   c   x���1�P�)�������q��c�5��עaA�*��L�p���O���S���|��9�B�T���dSF|�q$�,d�T�j��4��?@��     