%% Load data file
data = readmatrix("data\single_test_1.csv");
t = (data(:, 1));
sig = (data(:, 2));

% Palette
dotColor  = [0.55 0.71 0.86];
lineColor = [0.90 0.60 0.65];
textColor = [0.25 0.25 0.30];
gridColor = [0.85 0.85 0.88];

%% Figure 1
figure('Color', 'w', 'Position', [100 100 900 550])
scatter(t, sig, 70, dotColor, 'filled', 'MarkerFaceAlpha', 0.8, ...
    'MarkerEdgeColor', 'none')
hold on
%plot(t, sig, 'Color', lineColor, 'LineWidth', 3)
hold off
styleAxes(gca, textColor, gridColor)
title('HMC 1021', 'FontSize', 24, 'FontWeight', 'normal', 'Color', textColor)
xlabel('Time [s]', 'FontSize', 18)
ylabel('Signal [V]', 'FontSize', 18)
legend('Data', 'FontSize', 14, 'TextColor', textColor, ...
    'Box', 'off', 'Location', 'northwest')

%% Style-funktion, (TODO: Skift farver til at matche forside)
function styleAxes(ax, textColor, gridColor)
set(ax, 'FontName', 'Helvetica', 'FontSize', 16, ...
    'Box', 'off', 'TickDir', 'out', 'TickLength', [0 0], ...
    'LineWidth', 1, 'Layer', 'bottom')
ax.YGrid = 'on';
ax.XGrid = 'off';
ax.GridColor = gridColor;
ax.GridAlpha = 1;
ax.XAxis.Color = gridColor;
ax.YAxis.Color = gridColor;
ax.XAxis.Label.Color = textColor;
ax.YAxis.Label.Color = textColor;
ax.XAxis.TickLabelColor = textColor;
ax.YAxis.TickLabelColor = textColor;
end