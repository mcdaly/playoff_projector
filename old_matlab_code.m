function playoff_possibilies
records = [10 2 0;
    8 4 0;
    7 5 0;
    5 7 0;
    6 6 0;
    7 5 0;
    5 6 1;
    6 6 0;
    5 7 0;
    6 6 0;
    3 9 0;
    3 8 1];

matchups = [8 3;
    9 4;
    10 5;
    1 6;
    11 7;
    12 2];

total_points = [1212; 1094; 1082; 946; 1021; 118; 789; 1094; 1028; 1071; 917; 917];
team_names = {'Hos-', 'Olbert-', 'Daly-', 'Quinn-', 'Cakes-', 'Baker-', 'Yanni-', 'Provost-', 'Evan-', 'Amrit-', 'Kyle-', 'Devon-'};
outcomes = 1:2;
% 1 = First Team Wins, 2 = Second Team Wins, 3 = Tie
for a = outcomes
    a_record = records;
    if a == 1
        a_record = add_win(a_record,matchups(1,1));
        a_record = add_loss(a_record,matchups(1,2));
    elseif a == 2
        a_record = add_win(a_record,matchups(1,2));
        a_record = add_loss(a_record,matchups(1,1));
    elseif a == 3
        a_record = add_tie(a_record,matchups(1,2));
        a_record = add_tie(a_record,matchups(1,1));
    end
    for b = outcomes
        b_record = a_record;
        if b == 1
            b_record = add_win(b_record,matchups(2,1));
            b_record = add_loss(b_record,matchups(2,2));
        elseif b == 2
            b_record = add_win(b_record,matchups(2,2));
            b_record = add_loss(b_record,matchups(2,1));
        elseif b == 3
            b_record = add_tie(b_record,matchups(2,2));
            b_record = add_tie(b_record,matchups(2,1));
        end
        for c = outcomes
            c_record = b_record;
            if c == 1
                c_record = add_win(c_record,matchups(3,1));
                c_record = add_loss(c_record,matchups(3,2));
            elseif c == 2
                c_record = add_win(c_record,matchups(3,2));
                c_record = add_loss(c_record,matchups(3,1));
            elseif c == 3
                c_record = add_tie(c_record,matchups(3,2));
                c_record = add_tie(c_record,matchups(3,1));
            end
            for d = 1
                d_record = c_record;
                if d == 1
                    d_record = add_win(d_record,matchups(4,1));
                    d_record = add_loss(d_record,matchups(4,2));
                elseif d == 2
                    d_record = add_win(d_record,matchups(4,2));
                    d_record = add_loss(d_record,matchups(4,1));
                elseif d == 3
                    d_record = add_tie(d_record,matchups(4,2));
                    d_record = add_tie(d_record,matchups(4,1));
                end
                for e = outcomes
                    e_record = d_record;
                    if e == 1
                        e_record = add_win(e_record,matchups(5,1));
                        e_record = add_loss(e_record,matchups(5,2));
                    elseif e == 2
                        e_record = add_win(e_record,matchups(5,2));
                        e_record = add_loss(e_record,matchups(5,1));
                    elseif e == 3
                        e_record = add_tie(e_record,matchups(5,2));
                        e_record = add_tie(e_record,matchups(5,1));
                    end
                    for f = 1
                        f_record = e_record;
                        if f == 1
                            f_record = add_win(f_record,matchups(6,1));
                            f_record = add_loss(f_record,matchups(6,2));
                        elseif f == 2
                            f_record = add_win(f_record,matchups(6,2));
                            f_record = add_loss(f_record,matchups(6,1));
                        elseif f == 3
                            f_record = add_tie(f_record,matchups(6,2));
                            f_record = add_tie(f_record,matchups(6,1));
                        end

                        final_record{a,b,c,d,e,f} = f_record;

                    end
                end
            end
        end
    end
end

% final_record = reshape(final_record, prod(size(final_record)), 1);
count = 0;
playoff_teams = zeros(length(records(:,1)),1);
tiebreaker_teams = zeros(length(records(:,1)),1);
team_size = 11;
all.hos_1 = cell(prod(size(f_record)),team_size);
all.olbert_2 = cell(prod(size(f_record)),team_size);
all.daly_3 = cell(prod(size(f_record)),team_size);
all.quinn_4 = cell(prod(size(f_record)),team_size);
all.cakes_5 = cell(prod(size(f_record)),team_size);
all.baker_6 = cell(prod(size(f_record)),team_size);
all.yanni_7 = cell(prod(size(f_record)),team_size);
all.provost_8 = cell(prod(size(f_record)),team_size);
all.evan_9 = cell(prod(size(f_record)),team_size);
all.amrit_10 = cell(prod(size(f_record)),team_size);
all.kyle_11 = cell(prod(size(f_record)),team_size);
all.devon_12 = cell(prod(size(f_record)),team_size);

for a = 1:length(final_record(:,1,1,1,1,1))
    if a == 1
        a_result = 'Joe Wins and Daly Loses';
    elseif a == 2
        a_result = 'Joe Loses and Daly Wins';
    end
    for b = 1:length(final_record(1,:,1,1,1,1))
        if b == 1
            b_result = 'Evan Wins and Quinn Loses';
        elseif b == 2
            b_result = 'Evan Loses and Quinn Wins';
        end
        for c = 1:length(final_record(1,1,:,1,1,1))
            if c == 1
                c_result = 'Amrit Wins and Cakes Loses';
            elseif c == 2
                c_result = 'Amrit Loses and Cakes Wins';
            end
            for d = 1:length(final_record(1,1,1,:,1,1))
                if d == 1
                    d_result = 'Hos Wins and Baker Loses';
                elseif d == 2
                    d_result = 'Hos Loses and Baker Wins';
                end
                for e = 1:length(final_record(1,1,1,1,:,1))
                    if e == 1
                        e_result = 'Kyle Wins and Yanni Loses';
                    elseif e == 2
                        e_result = 'Kyle Loses and Yanni Wins';
                    end
                    for f = 1:length(final_record(1,1,1,1,1,:))
                        if f == 1
                            f_result = 'Devon Wins and Olbert Loses';
                        elseif f == 2
                            f_result = 'Devon Loses and Olbert Wins';
                        end
                        win_percentage = (final_record{a,b,c,d,e,f}(:,1)+final_record{a,b,c,d,e,f}(:,3)*0.5)/13;
                        [val, team] = sort(win_percentage,'descend');
                        tiebreaker_inds = find(val(6) == val);
                        if any(tiebreaker_inds > 6)
                            end_team = tiebreaker_inds(1)-1;
                            tiebreaker_teams(team(tiebreaker_inds)) = tiebreaker_teams(team(tiebreaker_inds)) + 1;
                        else
                            end_team = 6;
                            tiebreaker_inds = [];
                        end
                        playoff_teams(team(1:end_team)) = playoff_teams(team(1:end_team)) + 1;
                        count = count + 1;
                        spots_battling_for = sum(tiebreaker_inds <= 6);

                        names = fieldnames(all);
                        for m = 1:numel(names)
                            [opponents, points_ahead] = tiebreak_opponents(team(tiebreaker_inds),spots_battling_for,m, total_points);
                            opponent_names = get_opponent_names(opponents, team_names);
                            if any(m==(team(tiebreaker_inds)))
                                tiebreaker_spots = spots_battling_for;
                            else
                                tiebreaker_spots = 0;
                            end
                            all.(names{m})(count,:) = {any(m==team(1:end_team)) any(m==(team(tiebreaker_inds))) a_result b_result c_result d_result e_result f_result tiebreaker_spots opponent_names points_ahead};
                        end
                    end
                end
            end
        end
    end
end

1
end


function [record] = add_win(record,team)
record(team,1) = record(team,1) + 1;
end

function [record] = add_loss(record,team)
record(team,2) = record(team,2) + 1;
end

function [record] = add_tie(record,team)
record(team,3) = record(team,3) + 1;
end

function [opponents, points_to_win] = tiebreak_opponents(tied_teams, spots_battling_for, current_team, total_points)
if ismember(current_team, tied_teams)
    opponents = tied_teams(tied_teams ~= current_team);
    points_to_win = total_points(current_team) - total_points(opponents);
else
    opponents = [];
    points_to_win = [];
end
end

function [opponent_names] = get_opponent_names(opponents, team_names)
if ~isempty(opponents)
%     opponent_names = {};
%     for i = 1:length(opponents)
%         opponent_names = strcat(opponent_names, team_names{opponents(i)});
%     end
    opponent_names = strcat(team_names{opponents});
else
    opponent_names = {};
end

end
