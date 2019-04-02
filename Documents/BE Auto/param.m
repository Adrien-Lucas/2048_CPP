%% BE 1
% LOIC FAUCHER ; ADRIEN LUCAS
clear all
close all
clc

%% Déclaration params
k=20;
M = 1;
b = 10;


%% Fonction de transfert
H2=tf([1/k],[M/k b/k 1]);

%% Réponse indicielle
step(H2)


%% Mesures
p = pole(H2)
%pzmap(H2)
% Système stable car poles à parties réelles strictement négatives seulement

%Gain statique mesuré : 0.05
%Ce qui correspond au gain de la fonction de transfert 1/k = 1/20 = 0.05

%Temps de réponse à 5% mesuré : Tr = 1.26s
%Par le calcul on trouve le coeff d'amortissement xi = b/(2sqrt(kM)) = 1.12
%Par les abaques on trouve Tr*2PI/wn = 1.1 => Tr = 1.54s


%impulse(H2)
grid on

%% Correcteur proportionnel
Kp = 230;
Kd = 0;
Ki = 0;

sim("chariot_bf", [0 3])
figure(1)
plot(x.time, x.signals.values)
grid on

%Mesures graphiques :
%Gain statique = 0.92
%Dépassement = (1.24 - 0.92)/0.92 * 100 = 34%
%Erreur statique = 1 - 0.92 = 0.08
%Temps de Réponse à 5% par zoom successifs = 0.5s

Hbo = Kp * H2;
Hbf = feedback(Hbo, 1);
%step(Hbf)

%Nouvelles mesures avec step :
%Gain statique = 0.92
%Dépassement = (1.24 - 0.92)/0.92 * 100 = 35.1%
%Erreur statique = 1 - 0.92 = 0.08
%Temps de Réponse à 5% = 0.503s

%Calculs validés !

%La perturbation ajoute une modification du système de l'ordre de 10^-4
%(0.4mm au sens physique)
%% Correcteur proportionnel_intégral
Kp = 38;
Ki = 70;
Kd = 0;
sim("chariot_bf", [0 5])
figure(1)
plot(x.time, x.signals.values)
grid on

%Mesures graphiques :
%Gain statique = 0.9998
%Pas de dépassement
%Erreur statique = 1 - 0.9998 = 0.0002
%Temps de Réponse à 5% par zoom successifs = 0.5s

Kdep = tf([Kp Ki],[1 0])
Hbo = Kdep * H2;
Hbf = feedback(Hbo, 1);
%step(Hbf)

%Nouvelles mesures avec step :
%Gain statique = 1
%Pas de dépassement
%Erreur statique = 1 - 1 = 0
%Temps de Réponse à 5% = 0.505s

%La perturbation ajoute une modification nulle au système, elle est
%absorbée

%% Correcteur proportionnel_intégral_dérivé
Kp = 60;
Ki = 120;
Kd = 6;
sim("chariot_bf", [0 5])
figure(1)
plot(x.time, x.signals.values)
grid on

%Mesures graphiques :
%Gain statique = 1
%Pas de dépassement
%Erreur statique = 1 - 1 = 0
%Temps de Réponse à 5% par zoom successifs = 0.5s

Kdep = tf([Kd Kp Ki],[1 0]);
Hbo = Kdep * H2;
Hbf = feedback(Hbo, 1);
step(Hbf)

%Nouvelles mesures avec step :
%Gain statique = 1
%Pas de dépassement
%Erreur statique = 1 - 1 = 0
%Temps de Réponse à 5% = 0.499s

%La perturbation ajoute une modification nulle au système, elle est
%absorbée

%Conclusion : Le correcteur proportionnel intégral dérivé est le plus
%précis de tous les correcteurs car il a l'erreur statique la plus faible
%(quasi nulle), de plus les perturbations sont totalement absorbées par les
%correcteurs PI et PID, non par le correcteur P.
%De plus le correcteur PID n'a pas d'oscillations