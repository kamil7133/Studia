function fraktal(jakiZbior, pot, c, rGran, ReMin, ReMax, ImMin, ImMax, maxIter)
    % Ustawienia siatki
    xResolution = 800;
    yResolution = 800;
    x = linspace(ReMin, ReMax, xResolution);
    y = linspace(ImMin, ImMax, yResolution);

    % Macierz wyników
    Z = zeros(yResolution, xResolution);

    % Obliczenia
    for m = 1:length(x)
        for n = 1:length(y)
            if strcmp(jakiZbior, 'Mandelbrot')
                z = 0;                % Zbiór Mandelbrota, zaczynamy od z0 = 0
                c = x(m) + 1i*y(n);    % Każdy punkt to c w przestrzeni (Re, Im)
            elseif strcmp(jakiZbior, 'Julia')
                z = x(m) + 1i*y(n);    % Zbiór Julii, zaczynamy od punktu (z0)
            end

            iter = 0;
            while abs(z) <= rGran && iter < maxIter
                z = z^pot + c;  % Równanie iteracyjne
                iter = iter + 1;
            end
            Z(n, m) = iter;  % Zapisujemy liczbę iteracji
        end
    end

    % Wizualizacja
    imagesc(x, y, Z);
    axis xy;
    colormap(hot);
    colorbar;
    title(['Fraktal ' jakiZbior]);
end


%Przykładowe wywołania
%fraktal('Mandelbrot', 2, 0, 2, -2, 1, -1.5, 1.5, 100);

%fraktal('Julia', 2, -0.7 + 0.27015i, 2, -1.5, 1.5, -1.5, 1.5, 100);